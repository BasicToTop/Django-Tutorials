from testapp.models import Employee
from faker import Faker

faker = Faker()


def generate_fake_data(n):
    for _ in range(n):
        first_name = faker.first_name()
        email = faker.email()
        phone_number = faker.phone_number()
        print(
            f"Generated Fake Data - Name: {first_name}, Email: {email}, Phone: {phone_number}")
        print('*' * 40, _)


# n = int(input("Enter number of fake employees to generate: "))
# generate_fake_data(n)

def create_fake_employees(n):
    for _ in range(n):
        first_name = faker.first_name()
        middle_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.unique.email()
        phone_number = faker.phone_number()
        position = faker.job()
        doj = faker.date_this_decade()
        salary = round(faker.random_number(digits=5), 2)
        # data = {
        #     "first_name": first_name,
        #     "middle_name": middle_name,
        #     "last_name": last_name,
        #     "email": email,
        #     "phone_number": phone_number,
        #     "position": position,
        #     "doj": doj,
        #     "salary": salary
        # }
        # print('data ', data)

        employee = Employee(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            position=position,
            doj=doj,
            salary=salary,
            is_active=True
        )
        employee.save()
        print(f"Created Employee: {employee}")


n = int(input("Enter number of fake employees to create: "))
create_fake_employees(n)
print(f" {n} Fake employee creation completed.")
