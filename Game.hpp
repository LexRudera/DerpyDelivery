#ifndef GAME_H
#define GAME_H
#include <string>

class Game
{
    public:
        /** Default constructor */
        Game();
        /** Default destructor */
        virtual ~Game();
        void Run(std::string& EndMessage);
    protected:
    private:
};

#endif // GAME_H
