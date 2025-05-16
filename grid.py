class Grid():

    __CONSTANTE_GRID_INITAL =" 🏻"

    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y

        self.__initialize_grid()

    def __initialize_grid(self):
        self.grid_life = []
        for x in range(0, self.dim_x):
            sub_grid_life = []
            for y in range(0, self.dim_y):
                sub_grid_life.append(self.__CONSTANTE_GRID_INITAL)
            self.grid_life.append(sub_grid_life)

    def show_map(self):
        for x in range(0, self.dim_x):
            for y in range(0, self.dim_y):
                print(self.grid_life[x][y], end="")
            print()

def main():
    my_world_map = Grid(5,5)
    my_world_map.show_map()
    

if __name__ == "__main__":
        main()
    