#include <iostream>
#include <array>
//#include <dynarray>
#include <ctime>
#include <cstdlib>
#include <math.h>
#include <thread>

using namespace std;
// TOOD - Use array<> instead of builtin array
// TODO - Fix print statements
class SimulatedAnnealing
{   
    std::array<int, 50> queens;
    int n;
    public:
    SimulatedAnnealing(std::array<int, 50> queens, const unsigned int n);
    void run();
    void anneal();
    int cost(std::array<int, 50> board);
    std::array<int, 50> randomNeighbour();
    void printBoard();
};

SimulatedAnnealing::SimulatedAnnealing(std::array<int, 50> queens, const unsigned int n)
{
    this->queens = queens;
    this->n = n;
    run();
    // printBoard();
    
    // anneal();
    // printBoard();
    //for (int i = 0; i < n; i++) cout << randomNeighbour()[i];
}

void SimulatedAnnealing::run()
{
    printBoard();
    
    anneal();
    printBoard();
}

void SimulatedAnnealing::anneal()
{
    clock_t begin = clock();
    int currentCost = cost(queens);

    while (cost(queens) != 0)
    {
        float T = 1.0f;
        float T_min = 0.0001f;
        float alpha = 0.9f;

        while (T > T_min)
        {
            int i = 1;

            if (currentCost == 0 && T <= T_min)
            {
                cout << "  \rCost: " << currentCost << std::flush;
            }
            else{
                cout << "  \rCost: " << currentCost << " Queens: " << n << std::flush;
            }

            while (i <= 200)
            {
                std::array<int, 50> nextState = randomNeighbour();

                int nextCost = cost(nextState);

                float a = exp(-(nextCost - currentCost)/T);

                if (a > rand() % 101)
                {
                    queens = nextState;
                    
                    currentCost = nextCost;
                    if (currentCost == 0){
                        break;
                    }
                
                }
                i++; 
            }
            if (currentCost == 0)
            {
                break;
            }
            T = T*alpha;
        }
    }
    cout << "  \rCost: " << currentCost << " Queens: " << n << std::flush;
    clock_t end = clock();
    double time = double(end - begin) / CLOCKS_PER_SEC;
    cout << "\nTime: " << time << end;
}

std::array<int, 50> SimulatedAnnealing::randomNeighbour()
{
    // Select a random row and column for the random neighbour
    int i = rand() % n+1;
    int j = rand() % n+1;
    
    std::array<int, 50> queensTemp = queens;
    queensTemp[i] = j;

    return queensTemp;
}

int SimulatedAnnealing::cost(std::array<int, 50> board)
{
    int conflicts = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (i != j)
            {
                // Horizontal Axis
                if (board[i] == board[j])
                {
                    conflicts++;
                }
                // Positive Diagonal Axis
                if (abs(board[i] - board[j]) == abs(i - j))
                {
                    conflicts++;
                }
            }
        }
    }
    return conflicts;
}

void SimulatedAnnealing::printBoard()
{
    cout << "\n" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << "|";
        for (int j = 0; j < n; j++)
        {
            if (queens[j] == i)
            {
                cout << " X |";
            }
            else{
                cout << "   |";
            }
        }
        cout << "\n";
    }
}


int main(int argc, char **argv) {
    unsigned int cores = std::thread::hardware_concurrency();
    std::cout << cores << " concurrent threads are supported.\n";
    std::array<int, 50> queens;
    //printf("\nNumber of Queens: ");
    const unsigned int n = atoi(argv[1]);
    
    srand(time(0));
    for (int i = 0; i < n; i++) {
        queens[i] = rand() % n + 1;
    }
    //SimulatedAnnealing sa = SimulatedAnnealing(queens, n);
    std::thread t1(&SimulatedAnnealing::run, ref(queens), ref(n));
    //std::thread t2(&SimulatedAnnealing::run, ref(queens), ref(n));
    // std::thread t3(&SimulatedAnnealing::run, queens, n);
    // std::thread t4(&SimulatedAnnealing::run, queens, n);
    t1.join();
    //t2.join();
    // t3.join();
    // t4.join();
    printf("\nEnter a character to exit:");
    getchar();
    return 0;
}