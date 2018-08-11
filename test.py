from click.testing import CliRunner

from main import cli

from core import storage


def test_integration_commands():
    runner = CliRunner()

    clear_command(runner)
    start_command(runner)
    edit_command(runner)
    finish_command(runner)
    register_command(runner)
    remove_command(runner)
    show_command(runner)


def clear_command(runner):
    result = runner.invoke(cli, ['clear'], input='y')

    assert result.exit_code == 0
    assert 'All tasks were deleted successfully.' in result.output


def start_command(runner):
    result = runner.invoke(
        cli,
        ['start', '-m', 'Testing', '-t', '2h', '-c', 'mycategory', '-p', 'project', '-l', 'http://google.com']
    )
    assert result.exit_code == 0

    expected_output = 'The task 1 - "Testing" was started with success.\n'
    assert expected_output == result.output


def finish_command(runner):
    result = runner.invoke(cli, ['finish'])
    assert result.exit_code == 0

    expected_output = 'The last task 1 was finished with success.\n'
    assert expected_output == result.output

    # Testing a double finish command
    result = runner.invoke(cli, ['finish'])
    assert result.exit_code == 1

    expected_output = 'The last task 1 is already finished.\n'
    assert expected_output == result.output

    # Testing finish command when task doesn't exist
    result = runner.invoke(cli, ['finish', '2'])
    assert result.exit_code == 1

    expected_output = 'Task 2 not found.\n'
    assert expected_output == result.output


def edit_command(runner):
    result = runner.invoke(
        cli,
        ['edit', '1', '-m', 'New message', '-t', '1h', '-c', '', '-p', '', '-l', '']
    )
    assert result.exit_code == 0

    expected_output = (
        "The task 1 was edited with success. "
        "Fields changed: ['message', 'time', 'project', 'category', 'links']\n"
    )
    assert expected_output == result.output

    # Testing when sending the same data
    result = runner.invoke(
        cli,
        ['edit', '1', '-m', 'New message']
    )
    assert result.exit_code == 1

    expected_output = "No changes made to the task 1.\n"
    assert expected_output == result.output

    # Testing when the task doesn't exist
    result = runner.invoke(cli, ['edit', '2', '-m', 'New message'])
    assert result.exit_code == 1

    expected_output = 'Task 2 not found.\n'
    assert expected_output == result.output


def register_command(runner):
    result = runner.invoke(
        cli,
        ['register', '-m', 'Testing', '-t', '2h', '-c', 'mycategory', '-p', 'project', '-l', 'http://google.com']
    )
    assert result.exit_code == 0

    expected_output = 'The task 2 - "Testing" was registered with success.\n'
    assert expected_output == result.output


def remove_command(runner):
    result = runner.invoke(cli, ['remove', '2'], input='y')

    assert result.exit_code == 0
    assert 'The task 2 was removed with success.' in result.output


def show_command(runner):
    result = runner.invoke(cli, ['show', '1'])

    task = storage.get_by_id('1')

    task_1 = f"{task.id};{task.message};{task.time};{task.project};{task.category}"

    assert task_1 in result.output
    assert result.exit_code == 0

    # Testing show in reverse order and limit
    register_command(runner)

    result = runner.invoke(cli, ['show', '--tail', '--limit', '1'])
    task = storage.get_by_id('2')

    task_2 = f"{task.id};{task.message};{task.time};{task.project};{task.category}"

    assert task_2 in result.output
    assert task_1 not in result.output
    assert result.exit_code == 0

    # Testing show when task doesn't exist
    result = runner.invoke(cli, ['show', '3'])

    expected_output = f"Task 3 not found.\n"

    assert expected_output == result.output
    assert result.exit_code == 1


if __name__ == '__main__':
    test_integration_commands()
