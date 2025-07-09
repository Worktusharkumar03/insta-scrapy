# Main entry point
import argparse
import yaml
from agent_orchestrator import run_pipeline

def main():
    parser = argparse.ArgumentParser(description='Instagram Video Scraper + Transcriber + Rewriter')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to config file')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    run_pipeline(config)

if __name__ == '__main__':
    main()
