#ifndef CONTROLBASE_H
#define CONTROLBASE_H

#include "Object.hpp"
namespace me
{
    class ControlBase : public Object, public sf::Transformable
    {
        public:
            ControlBase();
            virtual ~ControlBase();
        protected:
        private:
    };
}

#endif // CONTROLBASE_H
