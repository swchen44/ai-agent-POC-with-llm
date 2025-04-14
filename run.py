
import logging
from workflows.design_pipeline import run_pipeline
from core.config import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    logger.info("🚀 Multi-Agent Design System Started")
    user_input = input("\n🧠 Describe the Wi-Fi feature you want to design: \n👉 ")

    try:
        state = run_pipeline(user_input)
        logger.info("✅ Pipeline complete. Final output keys: %s", list(state.keys()))
        print("\n📝 Final State:")
        for k, v in state.items():
            print(f"--- {k} ---\n{v[:500]}\n")
    except Exception as e:
        logger.error("❌ Pipeline execution failed: %s", str(e))


if __name__ == "__main__":
    main()
