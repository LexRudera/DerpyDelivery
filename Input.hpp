#ifndef INPUT_H
#define INPUT_H
#include <vector>

class Input
{
    public:
        /** Default constructor */
        /** Default destructor */
        virtual ~Input();
        static Input* GetInputSource(int i) {return s_inputs[i];}
        static Input* NewInput();
    protected:
    private:
        Input();
        // TODO: Find out why the s_inputs is an undefined reference
        static std::vector<Input*> s_inputs;
        //friend Game;
};

#endif // INPUT_H
