import discord
from discord.ext import commands
from google import genai
import os
import asyncio

# ⚠️ 환경 변수에서 키를 불러옵니다.
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 1. Gemini 클라이언트 초기화
# 환경 변수가 설정되지 않았을 경우 오류 발생
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")

try:
    client_ai = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Gemini 클라이언트 초기화 오류: API 키가 올바른 형식인지 확인하세요. {e}")
    exit()

# 모델 선택
GEMINI_MODEL = 'gemini-2.5-pro'

# 2. 디스코드 봇 클라이언트 초기화
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """봇이 성공적으로 로그인했을 때 호출됩니다."""
    print(f'로그인 성공: {bot.user.name} (ID: {bot.user.id})')
    # 봇이 서버에 연결된 후, 슬래시 명령어를 동기화합니다.
    try:
        # 전역 명령어 동기화
        synced = await bot.tree.sync()
        print(f"동기화된 슬래시 명령어: {len(synced)}개")
    except Exception as e:
        print(f"슬래시 명령어 동기화 중 오류 발생: {e}")


# 3. 슬래시 명령어 정의 (/gemini)
@bot.tree.command(name="gemini", description="Gemini AI에게 질문하고 답변을 받습니다.")
@discord.app_commands.describe(
    질문="Gemini에게 할 질문을 입력해주세요."
)
async def gemini_command(interaction: discord.Interaction, 질문: str):
    """
    디스코드의 슬래시 명령어 (/gemini)를 처리하고 일반 텍스트로 응답합니다.
    (질문자와 질문 내용이 답변 메시지 안에 포함되도록 수정되었습니다.)
    """
    # 응답 대기 메시지를 먼저 보냅니다.
    await interaction.response.defer(thinking=True)
    
    # Gemini 모델에 전달할 프롬프트 구성 (Gemini 모델이 답변만 하도록 유도)
    prompt = f"질문에 대해 답변해 주세요: {질문}"

    try:
        # 4. Gemini API 호출
        response = client_ai.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        gemini_response = response.text
        
        # 5. 응답 텍스트 생성 (질문 내용 포함)
        # Markdown을 사용하여 질문 내용을 강조합니다.
        
        header = f"**{interaction.user.name}님의 질문:** {질문}\n---\n"
        
        full_message = header + gemini_response

        # 디스코드 메시지 길이 제한 (2000자) 처리
        if len(full_message) > 2000:
            # 질문 헤더를 포함한 2000자 이내로 자릅니다.
            full_message = full_message[:1990] + "\n\n...(답변이 너무 길어 잘렸습니다.)"

        # 6. 최종 일반 텍스트 응답 전송
        await interaction.followup.send(full_message)

    except Exception as e:
        print(f"Gemini API 호출 중 오류 발생: {e}")
        await interaction.followup.send(
            "죄송합니다, AI 응답 처리 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.", 
            ephemeral=True
        )


# 7. 봇 실행
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN 환경 변수가 설정되지 않았습니다.")

try:
    bot.run(DISCORD_TOKEN)
except discord.HTTPException as e:
    if e.code == 4014:
        print("ERROR: Invalid Intents! Discord Developer Portal에서 Message Content Intent를 활성화했는지 확인하세요.")
    elif e.code == 4001:
        print("ERROR: 토큰이 유효하지 않습니다. DISCORD_BOT_TOKEN 환경 변수의 값을 다시 확인해주세요.")
    else:
        print(f"봇 실행 중 HTTP 오류 발생: {e}")
except Exception as e:
    print(f"봇 실행 중 오류 발생: {e}")
