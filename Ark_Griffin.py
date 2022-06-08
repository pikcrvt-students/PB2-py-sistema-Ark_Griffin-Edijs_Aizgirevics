"""
Author: Edijs Aizgirevics.

A system that makes it easy for teachers to teach and test students knowledge.
Introducing theory, tasks and tests inside the system.
"""

from os import system


def save_data(file_name, data):
    """Save data in file array.

    file_name - str
    data - str
    """
    file = open(file_name + '.txt', 'w', encoding='utf-8')
    file.write(''.join(data))
    file.close()


def save_summary(student_id, summary):
    """Save students answers.

    student_id - str
    answers - str
    """
    summary = str(summary)
    file = open('student_summary/' + student_id + '.txt',
                'a', encoding='utf-8')
    file.write(summary)
    file.write('\n')
    file.close()


def take_data(file_name):
    """Read file and returns data.

    >>> [take_data(theory)]
    Izteiksmi var sadalit reizinatajos ar dazadiem panemieniem: 
      iznesot kopigo reizinataju  pirms iekavam,
      lietojot saisinatas reizinasanas formulas,
      grupejot,
      izmantojot vienadojuma saknes.

    1. Kopiga reizinataja iznesana pirms iekavam
     
    Lieto, ja visi izteiksmes locekli satur vienu un to pasu reizinataju.

    Piemers:

    3x?7x^2 = x(3?7x)
    8y^6+6y^4 = y^4(8y^2+6)   vai   2y^4(4y^2+3)

    2. Saisinato reizinasanas formulu lietosana
      
    a^2?b^2 = (a?b)(a+b) - kvadratu starpiba
     
    a^2+2ab+b^2 = (a+b)^2 = (a+b)(a+b) - binoma summas kvadrats
     
    a^2?2ab+b^2 = (a?b)^2 = (a?b)(a?b) - binoma starpibas kvadrats
     
    a^3+b^3 = (a+b)(a^2?ab+b^2) - kubu summa 
     
    a^3?b^3 = (a?b)(a^2+ab+b^2) - kubu starpiba

    Piemers:

    4x^2?12x+9 = (2x)^2?2?2?3x+3^2= (2x?3)^2 = (2x?3)(2x?3)
    1?8x^3 = 1^3?(2x)^3 = (1?2x)(1^2+1?2x+(2x)^2) = (1?2x)(1+2x+4x^2)
    v^10?n^10 = (v^5)^2?(n^5)^2 = (v^5?n^5)(v^5+n^5)
    """
    file = open(file_name + '.txt', 'r', encoding='utf-8')
    file_content = file.read()
    file.close()
    data = file_content.split('\n')
    return data


# Choose user
print('User:\n\t1. teacher\n\t2. student')
role = 0
while role != 1 or role != 2:
    role = int(input('choice: '))
    if role == 1 or role == 2:
        break

# Theacher
if role == 1:
    system('cls')
    # Choose what to do
    print('User:\n\t1. Tasks\n\t2. Test\n\t3. Student summary')
    task_test = 0
    while task_test != 1 or task_test != 2 or task_test != 3:
        task_test = int(input('choice: '))
        if task_test == 1 or task_test == 2 or task_test == 3:
            break

    # Make tasks
    if task_test == 1:
        # Input task count
        task_count = int(input('Task count: '))
        input()
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
        input()

    # Make test
    if task_test == 2:
        # Input test
        test_task_count = int(input('Test task count: '))
        input()
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
        input()
    # Student summary fo teacher
    if task_test == 3:
        system('cls')
        student_id = 'student_summary/' + input('Student id: ')
        summary = take_data(student_id)
        test_tasks = take_data('test')
        summary_len = len(test_tasks)
        summary_len = summary_len // 2
        for i in range(0, summary_len):
            print(summary[i])
        input()
        system('cls')


# Student
if role == 2:
    system('cls')
    # Choose what to do
    print('1. Repeat theory\n2. Do tasks\n3. Do test\n')
    choise = 0
    while choise != 1 or choise != 2 or choise != 3:
        choise = int(input('choice: '))
        if choise == 1 or choise == 2 or choise == 3:
            break
    system('cls')
    # Theory
    if choise == 1:
        file = open('theory' + '.txt', 'r')
        file_content = file.read()
        file.close()
        print(file_content)
        input()
        system('cls')

    # Task
    if choise == 2:
        tasks = take_data('tasks')
        task_correct_answers = take_data('tasks_correct_answers')
        task_count = len(tasks)
        task_answers = []
        task_correct_answers_count = 0
        # Input student id
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
            input()
            system('cls')
        task_proc = 100 // task_count * task_correct_answers_count  # count %
        # Output summary
        print('Right answer count: ', task_correct_answers_count,
              'of', task_count, ' or', task_proc, '%')
        input()
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
        system('cls')
        for i in range(0, test_count):
            test_task = test_tasks[i]
            test_correct_answer = test_correct_answers[i]
            test_rezult = ''
            # Output test task
            print(test_task)
            # Input answer
            test_answer = input('answer: ')
            if test_answer == test_correct_answer:
                test_rezult = 'Right'
                test_correct_answers_count += 1
            test_answer = test_answer + (str(i + 1) +
                                         '. ' + test_answer +
                                         ' (' + test_rezult + ')')
            # Output rezult
            input()
            system('cls')
        test_proc = 100 // test_count * test_correct_answers_count  # Count %
        grade = test_proc // 100 # Count grade
        # Output and save summary
        summary = 'Test - right answer count: ', test_correct_answers_count,\
            'of', test_count, ' or', test_proc, '%', 'grade', grade
        print('Right answer count: ', test_correct_answers_count,
              'of', test_count, ' or', test_proc, '%', 'grade', grade)
        save_summary(student_id, summary)
        input()
        system('cls')

__version__ = 2
