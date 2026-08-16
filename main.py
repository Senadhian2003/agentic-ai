from agent import run_agent


def main():
    question = "Get information about Ben 10 from the internet and push it to the Discord server"
    answer = run_agent(question)
    print(answer)


if __name__ == "__main__":
    main()
