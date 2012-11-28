// The Global Functions
//------------------------------------------------------------------
// Functions and stuff that is globally accessible to the entire
// architecture of the game. Logging and error stuff for instance.

#ifndef GLOBAL_HPP_INCLUDED
#define GLOBAL_HPP_INCLUDED

#include <iostream>

namespace me
{
    void Error(std::string err);
    void CriticalError(std::string err);
    void Log(std::string txt);
}

#endif // GLOBAL_HPP_INCLUDED
