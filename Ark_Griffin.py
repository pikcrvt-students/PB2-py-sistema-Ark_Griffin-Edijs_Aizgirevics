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
    file.write(''.join(data))
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


def save_summary(student_id, summary):
    """Save students answers.

    student_id - str
    answers - str
    """
    summary = str(summary)
    file = open('student_summary/' + student_id + '.txt', 'a')
    file.write(summary)
    file.write('\n')
    file.close()


# Chose user
print('User:\n\t1. teacher\n\t2. student')
role = 0
while role != 1 or role != 2:
    role = int(input('choise: '))
    if role == 1 or role == 2:
        break

# Theacher
if role == 1:
    system('cls')

    # Chose what to do
    print('User:\n\t1. Tasks\n\t2. Test\n\t3. Student summary')
    task_test = int(input('choise: '))

    # Make tasks
    if task_test == 1:
        # Input task count
        task_count = int(input('Task count: '))
        system('pause')
        system('cls')
        tasks = [0] * task_count
        tasks_correct_answers = [0] * task_count

        for i in range(0, task_count):
            # Input task
            tasks[i] = input(str(i + 1) + '. task: ')

            # Input task answer
            tasks_correct_answers[i] = input('Task answer: ')

        save_data('tasks', tasks)
        save_data('tasks_correct_answers', tasks_correct_answers)
        system('pause')

    # Make test
    if task_test == 2:
        # Input test
        test_task_count = int(input('Test task count: '))
        system('pause')
        system('cls')
        test_task = [0] * test_task_count
        test_correct_answers = [0] * test_task_count

        for i in range(0, test_task_count):
            # Input task
            test_task[i] = input(str(i + 1) + '. task: ')

            # Input task answer
            test_correct_answers[i] = input('Task answer: ')

        save_data('test', test_task)
        save_data('test_correct_answers', test_correct_answers)
        system('pause')

    # Student summary fo teacher
    if task_test == 3:
        system('cls')
        student_id = 'student_summary/' + input('Student id: ')
        summary = take_data(student_id)

        tasks = take_data('tasks')
        task_count = len(tasks)
        test_tasks = take_data('test')
        test_count = len(test_tasks)
        summary_len = task_count + test_count
        summary_len = summary_len // 2
        for i in range(0, summary_len):
            print(summary[i])
        system('pause')
        system('cls')


# Student
if role == 2:
    system('cls')

    # Chose what to do
    print('1. Repeat theory\n2. Do tasks\n3. Do test\n')
    choise = int(input('choise: '))
    system('cls')

    # Theory
    if choise == 1:
        file = open('theory' + '.txt', 'r')
        file_content = file.read()
        file.close()
        print(file_content)
        system('pause')
        system('cls')

    # Task
    if choise == 2:
        tasks = take_data('tasks')
        task_correct_answers = take_data('tasks_correct_answers')
        task_count = len(tasks)
        task_answers = []
        task_correct_answers_count = 0

        # Input student id
        student_id = input('Input student id: ')
        system('pause')
        system('cls')

        for i in range(0, task_count):
            task = tasks[i]
            task_correct_answer = task_correct_answers[i]
            task_rezult = ''

            # Output task
            print(task)

            # Input answer
            task_answer = input('answer: ')

            if task_answer == task_correct_answer:
                task_rezult = 'Right'
                task_correct_answers_count += 1
            else:
                task_rezult = 'Wrong'

            task_answer = task_answer + (str(i + 1) + '. ' +
                                         str(task_answer) + ' (' +
                                         str(task_rezult) + ')')

            # Output rezult
            print(task_rezult)
            system('pause')
            system('cls')

        task_proc = 100 // task_count * task_correct_answers_count  # count %

        # Output and save summary
        summary = 'Tasks - right answer count: ', task_correct_answers_count, 'of', task_count, ' or', task_proc, '%'
        print('Right answer count: ', task_correct_answers_count,
              'of', task_count, ' or', task_proc, '%')
        save_summary(student_id, summary)
        system('pause')
        system('cls')

    # Test
    if choise == 3:
        test_tasks = take_data('test')
        test_correct_answers = take_data('test_correct_answers')
        test_count = len(test_tasks)
        test_answers = []
        test_correct_answers_count = 0

        # Input student id
        student_id = input('Input student id: ')
        system('pause')
        system('cls')

        for i in range(0, test_count):
            test_task = test_tasks[i]
            test_correct_answer = test_correct_answers[i]
            rezult = ''

            # Output test task
            print(test_task)

            # Input answer
            test_answer = input('answer: ')
            if test_answer == test_correct_answer:
                test_rezult = 'Right'
                test_correct_answers_count += 1
            else:
                test_rezult = 'Wrong'

            test_answer = test_answer + (str(i + 1) + '. ' + test_answer + ' (' + test_rezult + ')')

            # Output rezult
            print(rezult)
            system('pause')
            system('cls')

        test_proc = 100 // test_count * test_correct_answers_count  # count %

        # Output and save summary
        summary = 'Test - right answer count: ', test_correct_answers_count, 'of', test_count, ' or', test_proc, '%'
        print('Right answer count: ', test_correct_answers_count,
              'of', test_count, ' or', test_proc, '%')
        save_summary(student_id, summary)
        system('pause')
        system('cls')

__version__ = 2
