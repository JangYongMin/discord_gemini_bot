🤖 Discord Gemini 챗봇 (슬래시 명령어 기반)

이 프로젝트는 Python의 discord.py 라이브러리와 Google의 google-genai 라이브러리를 사용하여 구현된 디스코드 챗봇입니다. 사용자의 질문을 Gemini AI 모델에 전달하고, 그 답변을 디스코드 채널에 깔끔한 Embed 메시지 형태로 전송합니다.

✨ 주요 특징

슬래시 명령어 (/gemini): 직관적인 사용자 경험을 제공합니다.

Embed 메시지: 질문 내용과 답변을 분리하여 채팅 기록에 명확하게 남깁니다.

Gemini AI 통합: 강력한 gemini-2.5-pro 모델을 사용하여 답변을 생성합니다.

안전한 환경 변수 관리: API 키와 봇 토큰이 코드 외부에 안전하게 보관됩니다.

🛠️ 준비 사항

봇을 실행하기 위해서는 다음 두 가지 키가 필요하며, 봇을 서버에 초대해야 합니다.

Gemini API Key

Google AI Studio에서 발급받습니다.

Discord Bot Token

Discord Developer Portal에서 봇을 생성하고 토큰을 발급받습니다.

필수 설정: 봇의 설정 페이지에서 **Message Content Intent**를 반드시 활성화해야 합니다.

봇 서버 초대

OAuth2 > URL Generator에서 bot 및 applications.commands 스코프를 선택하여 초대 링크를 생성하고 서버에 봇을 추가합니다.

📦 설치 및 실행 방법

1. 필수 라이브러리 설치

프로젝트가 있는 폴더에서 터미널을 열고 다음 명령어를 실행합니다.

pip install discord.py google-genai


2. 환경 변수 설정 (매우 중요!)

보안을 위해 봇 토큰과 API 키를 환경 변수로 설정해야 합니다. YOUR_..._KEY 부분을 실제 키 값으로 대체하세요.

Windows (PowerShell 권장)

$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
$env:DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"


Linux/macOS (Bash/Zsh)

export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
export DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"


💡 참고: 환경 변수는 해당 터미널 세션에만 유효합니다. 새 터미널을 열면 다시 설정해야 합니다.

3. 봇 파일 실행

환경 변수를 설정한 동일한 터미널에서 봇 파일(bot.py)을 실행합니다.

python bot.py


터미널에 "로그인 성공: [봇 이름]" 메시지가 표시되면 정상적으로 작동 중입니다.

💻 봇 사용 방법

봇이 온라인 상태일 때, 봇이 초대된 디스코드 채널에서 다음 절차를 따릅니다.

메시지 입력창에 / 를 입력합니다.

gemini 명령어를 선택합니다.

질문 필드에 AI에게 할 질문을 입력하고 Enter를 누릅니다.

봇은 질문 내용과 답변을 포함하는 Embed 메시지로 응답할 것입니다
