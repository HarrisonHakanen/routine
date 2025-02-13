import threading
from datetime import datetime, timedelta

class routine_thread:

    seconds = -1
    minute = -1
    hour = -1
    day = -1
    at = ""
    finish = False


    def __init__(self,func,seconds=-1,minute=-1,hour=-1,day=-1,at=""):
        self.seconds = seconds
        self.minute = minute
        self.hour = hour
        self.day = day
        self.at = at
        self.func = func


    def start(self):

        self.func()


class routine:

    routines = []
    dia_anterior = ""

    def newRoutine(self,func,seconds=-1,minute=-1,hour=-1,day=-1,at="",logs=False):

        self.routines.append(routine_thread(func,seconds,minute,hour,day,at))
        
    def start(self):

        existeThread = False


        for routine in self.routines:

            thread = threading.Thread(target=routine.start)
            

            if routine.at != "" and (routine.day > -1 and routine.day < 7):
                
                data_atual = datetime.now()
                dia_semana_numero = data_atual.weekday()
                hora_atual = datetime.now().strftime("%H:%M")
                
                hora_atual_time = datetime.strptime(hora_atual, "%H:%M").time()
                hora_compare_time = datetime.strptime(routine.at, "%H:%M").time()

                if routine.finish == False:

                    if routine.day == dia_semana_numero:
                        if hora_atual_time > hora_compare_time:
                            thread.start()
                            existeThread = True
                            routine.finish = True
                        

                else:

                    data_atual = datetime.now()
                    dia_semana_numero = data_atual.weekday()

                    if dia_semana_numero != routine.day:
                        routine.finish = False


            elif routine.at != "" and routine.day == -1:
                print(f"Must put ""at"" together with ""day""")


            elif routine.at == "" and routine.day > -1 and routine.day < 7:
                
                data_atual = datetime.now()
                dia_semana_numero = data_atual.weekday()

                if routine.day == dia_semana_numero:
                    if routine.finish == False:
                        
                        thread.start()
                        existeThread = True
                        
                        routine.finish = True

                else:
                    routine.finish = False


            elif routine.at != "" and routine.day == 7:

                hora_atual = datetime.now().strftime("%H:%M")
                
                hora_atual_time = datetime.strptime(hora_atual, "%H:%M").time()
                hora_compare_time = datetime.strptime(routine.at, "%H:%M").time()

                if routine.finish == False:

                    if hora_atual_time > hora_compare_time:
                        thread.start()
                        existeThread = True
                        routine.finish = True
                else:

                    data_atual = datetime.now()

                    if self.dia_anterior != data_atual.strftime("%Y-%m-%d"):
                        routine.finish = False


            elif routine.at == "" and routine.day == 7:

                data_atual = datetime.now()
                data_menos_dois = data_atual - timedelta(days=2)
                
                if self.dia_anterior == data_menos_dois.strftime("%Y-%m-%d") or self.dia_anterior == "":

                    thread.start()
                    existeThread = True
                    routine.finish = True


        #---------------------------------------------------------------
        if self.dia_anterior != "":

            data_atual = datetime.now()
            dia_anterior_compara = data_atual - timedelta(days=1)

            dia_anterior_compara_str = dia_anterior_compara.strftime("%Y-%m-%d")

            if self.dia_anterior != dia_anterior_compara_str:
                self.dia_anterior = dia_anterior_compara_str
        
        else:

            data_atual = datetime.now()
            dia_anterior_compara = data_atual - timedelta(days=1)

            dia_anterior_compara_str = dia_anterior_compara.strftime("%Y-%m-%d")
            self.dia_anterior = dia_anterior_compara_str
        #---------------------------------------------------------------



        if existeThread:
            thread.join()