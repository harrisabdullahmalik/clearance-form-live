# Django
from django.shortcuts import render, HttpResponse

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# Create your views here.


def index(request):
    if request.POST:
        login_data = request.POST.dict()
        reg_no = login_data.get("reg_no")
        location = login_data.get("inside-giki")
        birth_year = int(reg_no[0:4]) - 19

        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
        return HttpResponse(f"{birth_year}")
        #
        # count = 1
        # while count < 6:
        #     date = (birth_year * 10000) + 101
        #     for i in range(0, 383):
        #         try:
        #             if location == "inside-giki":
        #                 driver.get("http://clearance.giki.edu.pk:82/ranks/")
        #             else:
        #                 driver.get("http://clearance2.giki.edu.pk:8005/ranks/")
        #         except WebDriverException:
        #             return render(request, "index.html", {
        #                 "message": "ERR_CONNECTION_TIMED_OUT"
        #             })
        #
        #         username = driver.find_element(By.NAME, "username")
        #         password = driver.find_element(By.NAME, "password")
        #         username.send_keys(reg_no)
        #         password.send_keys(date)
        #         driver.find_element(By.NAME, "bt1").click()
        #
        #         if driver.current_url == "http://clearance2.giki.edu.pk:8005/ranks/ranks.php":
        #             registration = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[1]/td[2]").text
        #             name = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[2]/td[2]").text
        #             program = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[3]/td[2]").text
        #             sgpa = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[4]/td[2]").text
        #             cgpa = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[5]/td[2]").text
        #             s_rank_b = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[6]/td[2]").text
        #             c_rank_b = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[7]/td[2]").text
        #             s_rank_p = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[8]/td[2]").text
        #             c_rank_p = driver.find_element(By.XPATH, "//form/table[2]/tbody/tr[9]/td[2]").text
        #             driver.quit()
        #             # return render(request, "result.html", {
        #             #     "reg_no": registration,
        #             #     "name": name,
        #             #     "program": program,
        #             #     "sgpa": sgpa,
        #             #     "cgpa": cgpa,
        #             #     "s_rank_b": s_rank_b,
        #             #     "c_rank_b": c_rank_b,
        #             #     "s_rank_p": s_rank_p,
        #             #     "c_rank_p": c_rank_p,
        #             # })
        #             return HttpResponse(f"{name}")
        #         date += 1
        #         if date % 100 == 32:
        #             date -= 32
        #             date += 100
        #
        #     birth_year += pow(-1, count + 1) * count
        #     count += 1
        return render(request, 'index.html', {
            "message": "User not found"
        })
    else:
        return render(request, 'index.html')
