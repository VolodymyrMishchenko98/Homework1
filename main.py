vacation_spots = [
    {
        'title':'Python Developer',
        'location':'Remote',
        'salary':100000,
        'city':'San Francisco'
    },
    {
        'title':'Data Scientist',
        'location':'Remote',
        'salary':120000,
        'city':'San Francisco'
    },
    {
        'title':'Web Developer',
        'location':'Remote',
        'salary':90000,
        'city':'Los Angeles'
    },
    {
        'title':'Software Engineer',
        'location':'Remote',
        'salary':110000,
        'city':'Chicago'
    },
    {
        'title':'Frontend Developer',
        'location':'Remote',
        'salary':95000,
        'city':'Seattle'
    },
    {
        'title':'DevOps Engineer',
        'location':'Remote',
        'salary':115000,
        'city':'Boston'
    },
    {
        'title':'Full Stack Developer',
        'location':'Home',
        'salary':105000,
        'city':'Austin'
    },
    {
        'title':'Machine Learning Engineer',
        'location':'Remote',
        'salary':130000,
        'city':'Mountain View'
    },
    {
        'title':'Database Administrator',
        'location':'Home',
        'salary':98000,
        'city':'Denver'
    },
    {
        'title':'Cloud Architect',
        'location':'Home',    
        'salary':140000,
        'city':'Portland'
    }
]
while True:
    print('1 - Показ усіх вакансій \n 2 - Фільтр по місту \n 3 - Фільтр по зарплаті \n 4 - Тільки remote \n 5 - Пошук за назвою посади \n 6 - Вакансії, відсортовані по зарплаті \n 7 - Вакансії у конкретному місті \n 8 - Вийти')
    option = int(input('Your option: '))
    
    if option == 1:
        print('\n--- Усі вакансії ---')
        for spot in vacation_spots:
            print(f'{spot["title"]} в {spot["city"]} - {spot["salary"]} грн')
        print()
    
    elif option == 2:
        city = input('Введіть місто для фільтра: ')
        print(f'\n--- Вакансії в {city} ---')
        found = False
        for spot in vacation_spots:
            if city.lower() in spot['city'].lower():
                print(f'{spot["title"]} - {spot["salary"]} грн')
                found = True
        if not found:
            print(f'Вакансій в {city} не знайдено')
        print()
    
    elif option == 3:
        try:
            salary = int(input('Введіть зарплату для пошуку: '))
            print(f'\n--- Вакансії з зарплатою {salary} грн ---')
            found = False
            for spot in vacation_spots:
                if spot['salary'] == salary:
                    print(f'{spot["title"]} в {spot["city"]} - {spot["salary"]} грн')
                    found = True
            if not found:
                print(f'Вакансій з зарплатою {salary} не знайдено')
            print()
        except ValueError:
            print('Введіть коректне число!')
    
    elif option == 4:
        print('\n--- Тільки Remote вакансії ---')
        for spot in vacation_spots:
            if spot['location'].lower() == 'remote':
                print(f'{spot["title"]} - {spot["salary"]} грн')
        print()
    
    elif option == 5:
        job_title = input('Введіть назву вакансії для пошуку: ')
        print(f'\n--- Пошук за "{job_title}" ---')
        found = False
        for spot in vacation_spots:
            if job_title.lower() in spot['title'].lower():
                print(f'{spot["title"]} в {spot["city"]} - {spot["salary"]} грн ({spot["location"]})')
                found = True
        if not found:
            print(f'Вакансії з назвою "{job_title}" не знайдено')
        print()
    
    elif option == 6:
        print('\n--- Вакансії, відсортовані по зарплаті (від високої до низької) ---')
        sorted_spots = sorted(vacation_spots, key=lambda x: x['salary'], reverse=True)
        for i, spot in enumerate(sorted_spots, 1):
            print(f'{i}. {spot["title"]} в {spot["city"]} - {spot["salary"]} грн ({spot["location"]})')
        print()
    
    elif option == 7:
        job_city = input('Введіть назву міста для пошуку: ')
        print(f'\n--- Вакансії у місті {job_city} ---')
        found = False
        for spot in vacation_spots:
            if job_city.lower() in spot['city'].lower():
                print(f'{spot["title"]} - {spot["salary"]} грн ({spot["location"]})')
                found = True
        if not found:
            print(f'Вакансій у місті {job_city} не знайдено')
        print()
    
    elif option == 8:
        quit()
    
    else:
        print('Невідома опція. Спробуйте ще раз.')
        print()