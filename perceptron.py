import math     # A usar: floor
import pdb      # A usar: set_trace

class perceptron:
    def __init__(self, bits_to_index, global_history_size):
        #Escriba aquí el init de la clase
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0
        self.history_reg = [-1] * global_history_size        # BR history table inicializa en -1
        self.perceptron_table = list()  # Se genera la tabla de perceptrones
        for i in range(2 ** bits_to_index):
            hist_temp = []
            for j in range(global_history_size + 1):
                hist_temp.append(0) # Inicializa en 0
            self.perceptron_table.append(hist_temp)
        self.theta = math.floor(1.93 * global_history_size + 14)  # Umbral
        self.y_out = 0  # Salida anterior del cálculo de "y"
        # Inicia DEBUG
#        self.max = 0
#        self.min = 0
        # Fin DEBUG

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\t\t\tPerceptron")
        print("\tBits de la historia global:\t\t\t\t", str(len(self.history_reg)))
        print("\tCantidad de entradas en la tabla de perceptrones:\t", str(len(self.perceptron_table)))
        print("\tLongitud de cada entrada de la tabla de perceptrones:\t", str(len(self.perceptron_table[0])))
        

    def print_stats(self):
        print("Resultados de la simulación")
        print("\t# branches:\t\t\t\t\t\t"+str(self.total_predictions))
        print("\t# branches tomados predichos correctamente:\t\t"+str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente:\t\t"+str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente:\t\t"+str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente:\t"+str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken+self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas:\t\t\t\t"+str(formatted_perc)+"%")

    def predict(self, PC):
        """Método que obtiene la predicción al operar un perceptrón.

            Se encarga de calcular el índice de la tabla de perceptrones,
        calcular el calor de la variable interna "y" como el resultado del
        perceptrón.

        Parameters
        ----------
        self : 
            Permite acceder a las variables internas de la clase.

        PC : string
            Valor del contador de programa en el que se predicirá el salto.

        Returns
        -------
        resultado : string
            Resultado de la predicción realizada.

        """
        # Aquí va la célula del perceptrón
        index = int(PC) % len(self.perceptron_table)     # Índice del PC
        y_res = self.perceptron_table[index][0]  # Variable "y" del resultado
                                                 # Bias 
        # Se empieza por calcular el resultado del perceptrón
        for i in range(len(self.history_reg)):
            y_res += self.history_reg[i] * self.perceptron_table[index][i + 1]

        # Valor anterior de la suma de "y" para la condición de theta
        self.y_out = y_res

        # Inicio DEBUG
#        if ((y_res > 0) and (y_res > self.max)):
#            self.max = y_res
#        elif ((y_res < 0) and (y_res < self.min)):
#            self.min = y_res

#        for i in range(len(self.perceptron_table[index])):
#            if ((i > 0) and (i > self.max)):
#                self.max = i
#            elif ((i < 0) and (i < self.min)):
#                self.min = i

#        print("max: ", self.max, "min: ", self.min)
        # Fin DEBUG


        # Luego, se decide si se toma o no el salto
        if (y_res < 0):
            resultado = "N"
        else:
            resultado = "T"

        return resultado
  

    def update(self, PC, result, prediction):
        """Método que evalúa el resultado de la predicción y entrena los pesos.

            Se encarga de evaluar el resultado de la predicción respecto a qué
        hizo realmente el procesador. Entrena el vector de pesos de los
        perceptrones en caso de requerirlo. Además, actualiza las estadísticas
        que se reportan con la ejecución del programa.

        Parameters
        ----------
        self : 
            Permite acceder a las variables internas de la clase.

        PC : string
            Valor del contador de programa en el que se evaluará la predicción

        result : string
            Resultado final del branch.

        prediction : string
            Resultado de la predicción del perceptrón.

        Returns
        -------
        None
        """
        index = int(PC) % len(self.perceptron_table)     # Índice del PC
        # Variable t para el entreno de los pesos
        if (result == "T"):             # Variable para el cálculo de pesos
            t = 1                       # nuevos
        else: 
            t = -1

        # Condición de signo
        if (((self.y_out > 0) and (t > 0)) or ((self.y_out < 0) and (t < 0))):
            signo = False
        else:
            signo = True

        # Entrenamiento de los pesos:
        # Si se cumplen las condiciones, se entrena el valor de bias y se
        # recorre la longitud de la historia global y se suma al valor de
        # cada peso el producto de t por la entrada iterada de BHT
        if (signo or (abs(self.y_out) <= self.theta)):
            self.perceptron_table[index][0] += t
            for i in range(len(self.history_reg)):
                self.perceptron_table[index][i + 1] += t * self.history_reg[i]
                

        # Se actualiza el registro desplazante de la historia global
        if (result == "T"):
            self.history_reg.insert(0, 1)
        else:
            self.history_reg.insert(0, -1)  # Se usa -1 para los no tomados
        self.history_reg.pop()

        # Código del ejemplo del profesor: actualiza las estadísitcas
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
        else:
            self.total_not_taken_pred_taken += 1

        # Se suma 1 a la cantidad de predicciones hechas
        self.total_predictions += 1

