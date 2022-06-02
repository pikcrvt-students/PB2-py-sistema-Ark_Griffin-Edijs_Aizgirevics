"""
author: Edijs Aizgirevics.

A system that makes it easy for teachers to teach and test studentsknowledge.
Introducing theory, tasks and tests inside the system.
"""

from os import system


def save_data(file_name, data):
    """Save data in file array.

    file_name - str
    data - str
    """
    file = open(file_name + '.txt', 'w')
    file.write('\n'.join(data))
    file.close()


def take_data(file_name):
    """Read file and returns data.

    file_name - str
    """
    file = open(file_name + '.txt', 'r')
    file_content = file.read()
    file.close()
    data = file_content.split('\n')
    return data


def save_answer(student_id, answers):
    """Save students answers.

    student_id - str
    answers - str
    """
    file = open('skolnieku_atbildes.txt', 'a')
    file.write('\n' + student_id + '\n\n')
    file.write('\n'.join(answers))
    file.write('\n\n-----------\n')
    file.close()


def check(answer, correct_answer):
    """Check that the student's answer is correct.

    answer - str
    correct_answer -str
    """
    if answer == correct_answer:
        return 'Right'
    else:
        return 'Wrong'


# Chose user
print('User:\n\t1. theacher\n\t2. student')
role = int(input('choise: '))
system('cls')

# Theacher
if role == 1:
    tasks = []
    test_task = []
    correct_answers_task = []
    test_correct_answers = []

    print('User:\n\t1. Tasks\n\t2. Test')
    task_test = int(input('choise: '))

    if task_test == 1:
        # Input task count
        task_count = int(input('Task count: '))
        system('pause')
        system('cls')

        for i in range(task_count):
            # Input task
            task = input(str(i + 1) + '. task: ')
            tasks.append(task)

            # Input task answer
            correct_answer = input('Task answer: ')
            correct_answers_task.append(correct_answer)

        save_data('tasks', tasks)
        save_data('correct_answers_task', correct_answer)
        system('pause')

    if task_test == 2:
        # Input test
        test_task_count = int(input('Task count: '))
        system('pause')
        system('cls')

        for i in range(test_task_count):
            # Input task
            test_task = input(str(i + 1) + '. task: ')
            test_task = test_task + test_task

            # Input task answer
            test_correct_answer = input('Task answer: ')
            test_correct_answer = test_correct_answer + test_correct_answer

        save_data('test', test_task)
        save_data('test_correct_answers', test_correct_answer)
        system('pause')

# Student
if role == 2:

    # Chose what to do
    print('1. Repeat theory\n2. Do tasks\n3. Do test\n')
    choise = int(input('choise: '))
    system('cls')

    # Theory
    if choise == 1:
        file = open('theory' + '.txt', 'r')
        file_content = file.read()
        print(file_content)
        file.close()
        system('pause')
        system('cls')


    # Task
    if choise == 2:
        tasks = take_data('tasks')
        task_correct_answers = take_data('correct_answers_task')
        task_count = len(tasks)
        task_answers = []
        task_correct_answers_count = 0

        # Input student id
        student_id = input('Input student id: ')
        system('pause')
        system('cls')

        for i in range(task_count):
            task = tasks[i]
            task_correct_answer = task_correct_answers[i]
            task_rezult = ''

            # Output task
            print(tasks)

            # Input answer
            task_answer = input('answer: ')
            task_rezult = check(task_answer, task_correct_answer)

            if task_rezult == 'Right':
                task_correct_answers_count += 1

            task_answer = task_answer + (str(i + 1) + '. ' + str(task_answer) + ' (' + str(task_rezult) + ')')

            # Output rezult
            print(task_rezult)
        task_proc = 100 / task_count * task_correct_answers_count  # count %

        # Output summery
        print('Right answer count: ', task_correct_answers_count, 'of', task_count, ' or', task_proc, '%')
        system('pause')
        system('cls')

    # Test
    if choise == 3:
        test_task = take_data('test')
        test_correct_answers = take_data('test_correct_answers')
        test_count = len(test_task)
        test_answers = []
        test_correct_answers_count = 0

        # Input student id
        student_id = input('Input student id: ')
        system('pause')
        system('cls')

        for i in range(0, test_count):
            test = test_task[i]
            correct_answer = test_correct_answers[i]
            rezult = ''

            # Output test task
            print(test_task)

            # Input answer
            test_answer = input('answer: ')
            test_rezult = check(test_answer, test_correct_answers)

            if rezult == 'Right':
                test_correct_answers_count += 1

            test_answer = test_answer + (str(i + 1) + '. ' + test_answer + ' (' + test_rezult + ')')

            # Output rezult
            print(rezult)
        test_proc = 100 / test_count * test_correct_answers_count  # count %

        # Output summery
        print('Right answer count: ', test_correct_answers_count, 'of', test_count, ' or', test_proc, '%')
        system('pause')
        system('cls')
