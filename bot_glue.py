from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.fallback import FallbackPolicy
import argparse
import warnings


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter(r".\models\NLU\model_20180601-022829")
    agent = Agent.load("models/current/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


fallback = FallbackPolicy(fallback_action_name="utter_default",
                          core_threshold=0.7,
                          nlu_threshold=0.4)

def train_dialogue(domain_file="./dialog_data/domain.yml",
                   model_path="./models/current/dialogue",
                   training_data_file="wine_stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3), KerasPolicy(), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=300,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent

if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices=["train-dialogue","run"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    if task == 'run':
        run()
    elif task == 'train-dialogue':
        train_dialogue()