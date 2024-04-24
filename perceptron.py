import math     # A usar: floor

class perceptron:
    def __init__(self, bits_to_index, global_history_size):
        #Escriba aquí el init de la clase
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0
        self.history_reg = [0] * global_history_size        # BR history table
        # Vector de pesos, el primero siempre es 1
        self.perceptron_weights = [1] + [0] * (global_history_size - 1)
        self.perceptron_table = [0] * (2 ** bits_to_index)  # Tabla perceptrón
        self.theta = math.floor((1.93 * global_history_size) + 14)  # Umbral

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tPerceptron")

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
        y_res = self.perceptron_weights[0]          # Variable "y" del resultado
        # Se empieza por calcular el resultado del perceptrón
        for i in range(1, len(self.history_reg)):
            y_res += self.history_reg[i] * self.perceptron_weights

        # Luego, se decide si se toma o no el salto
        if (y_res > 0):
            resultado = "T"
        else:
            resultado = "N"

        return resultado
  

    def update(self, PC, result, prediction):
        """Método que evalúa el resultado de la predicción y entrena los pesos.

            

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


        #Escriba aquí el código para actualizar
        #La siguiente línea es solo para que funcione la prueba
        #Quítela para implementar su código
        a = PC














































