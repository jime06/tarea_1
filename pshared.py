# import pdb
#código de simluador para un predictor p-shared.
"""
predictor p-shared: utiliza historia local. Donde tenemos una tabla con varios registros de historia. Además, mediante
el PC del branch se indexa una tabla que contiene un registro deslizante con la historia de los saltos que han ocurrido
para branches con un PC que terminan en los índices 00, 01, 10, 11.
"""

class pshared:
    def __init__(self, bits_to_index, local_history_size):
        self.bits_to_index = bits_to_index
        self.local_history_size = local_history_size
        pht_vals = [0 for i in range(2**local_history_size)] # Vals de inicio pht
        pht_indx = [i for i in range(2**local_history_size)] # Índices de pht
        self.pht = dict(zip(pht_indx, pht_vals))    # Se genera la tabla como
                                                    # diccionario
        pht_vals = [0 for i in range(2**bits_to_index)] # Vals de inicio bht
        pht_indx = [i for i in range(2**bits_to_index)] # Índices de bht
        self.bht = dict(zip(pht_indx, pht_vals))    # Se genera la tabla como
                                                    # diccionario
        # pdb.set_trace()
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

    def print_info(self): #información del predictor
        print("Parámetros del predictor:")
        print("\tTipo de predictor: \t\t\tpshared")
        print("\tBits de la indexados del PC: \t\t", self.bits_to_index)
        print("\tBits de la historia local: \t\t", self.local_history_size)

    def print_stats(self):
        print("Resultados de la simulación")
        print("\t# branches: \t\t\t\t\t\t" +str(self.total_predictions))
        print("\t# branches tomados predichos correctamente: \t\t" +str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente: \t\t" +str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente: \t\t" +str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente: \t\t" +str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken+self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas: \t\t\t\t" +str(formatted_perc)+ "%")


    def predict(self, PC): #acá se programa el funcionamiento del predictor
        # Índice de la tabla de historia local
        index_bht = int(PC) % len(self.bht)

        # Se obtiene el registro desplazante de la historia local,
        # como un valor entero. Este permite indexar la tabla pht
        local_hist = self.bht[index_bht]

        # Finalmente, se obtiene el valor del predictor de 2 bits
        pht_table_entry = self.pht[local_hist]

        # Con este valor, se puede realizar la predicción
        if (pht_table_entry in [2, 3]):
            return "T"
        else:
            return "N"


    def truncated_sum(self, valor, local_hist):
        # Realiza la suma truncada de valores a la tabla de predictores
        val_tmp = self.pht[local_hist] + valor
        if (val_tmp >= 3):
            self.pht[local_hist] = 3
        elif (val_tmp <= 0):
            self.pht[local_hist] = 0
        else: 
            self.pht[local_hist] = val_tmp


    def update(self, PC, result, prediction): #acá evaluamos el resultado de la predicción
        # Índice de la tabla de historia local
        index_bht = int(PC) % len(self.bht)

        # Se obtiene el registro desplazante de la historia local,
        # como un valor entero. Este permite indexar la tabla pht
        local_hist = self.bht[index_bht]

        # Finalmente, se obtiene el valor del predictor de 2 bits
        pht_table_entry = self.pht[local_hist]

        # Con los datos listos, se aplica la suma truncada
        if (result == "T"):
            self.truncated_sum(1, local_hist)
        else:
            self.truncated_sum(-1, local_hist)

        # Finalmente, se hace el shift lógico para agregar el
        # último resultado a la historia local
        # Es mañoso, yo sé, pero sirve
        self.bht[index_bht] = bin(self.bht[index_bht])[2:]  # Se obtiene el
                                                            # valor binario
                                                            # como una string
        # Se llena de ceros a la dimensión de la historia local
        self.bht[index_bht] = self.bht[index_bht].zfill(self.local_history_size)
        # Se agrega un cero o un no dependiendo del resultado
        if result == "T":
            self.bht[index_bht] = (self.bht[index_bht])[1:] + "1"
        else:
            self.bht[index_bht] = (self.bht[index_bht])[1:] + "0"
        # Se vuelve a base 10
        self.bht[index_bht] = int(self.bht[index_bht], 2)


        #actualiza stats
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1

        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1

        else:
            self.total_not_taken_pred_taken += 1

        self.total_predictions += 1

