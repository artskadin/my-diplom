# Мой диплом
В рамках дипломного проекта, который я сдал летом 2018 года, мной рассматривалось направление альтернативной энергетики. В частности была рассмотрена технология "Органический цикл Ренкина (ОЦР)", которая позволяет использовать/утилизировать низкопотенциальные источники тепла. Ввиду того, что при реализации рассматриваемой технологии имеется большой перечень рабочих веществ, на базе которых можно организовать процесс утилизации, возникла задача автоматизировать процесс подбора оптимального рабочего тела. Данное микро-веб-приложение было создано как раз с целью автоматизировать подбор оптимального рабочего тела. 

Само приложение написано на flask и обладает следующим функционалом:
* Позволяет получать информацию о веществах
* Позволяет получать по одним термодинамическим свойсвам другие
* Позволяет по заданным начальным параметрам подбирать оптимальное рабочее тело для установок, работающих на ОЦР.

За основу расчетов была взята библиотека термодинамических свойств CoolProp. Все логика прописана в пакете altenergy, где:
* calcprop - содержит одноименный модуль, где реализована логика расчета одних свойств на основе других
* fluidinfo - содержит одноименный модуль, позволяющий получать информацию о конкретном веществе
* predictor - содержит fluid_predictor.py , где реализован алгоритм расчета оптимального рабочего тела по начальным параметрам

Это был мой первый опыт работы с написанием веб-приложений на python.


# batchelor phases
Within the diploma project, which i passed last academic year, i considered the direction of alternative energy. In particular, "Organic Rankin Cycle (ORC) technology was considered. This technology allows to use/utilize low-potential heat sources. Due to the fact that this technology has a lot of working fluids on the basis of which it is possible to organize utilization process, the task arose to automate the process of selecting the optimal working fluid. this micro-web-application was created just to automate selection of the optimal fluid.

Web-app is created on flask and has the following functionality:
* It allows to get information abount certain fluid
* It allows to get one thermodynamic property to another
* It allows to select the optimal working fluid by initial parameters

This app bases on thermodynamic property library "CoolProp". "altenergy" contains logic of app, where:
* calcprop - contains the module of the same name, where the logic of calculation of some properties based on other
* fluidinfo - contains the module of the same name, which allow to recieve information about certain fluid
* predictor - contains fluid_predictor.py, where the algorithm for calculating the optimal working fluid according to the initial parameters
