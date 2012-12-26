#ifndef CONTROLBASE_H
#define CONTROLBASE_H

#include "Object.hpp"
namespace me
{
    class Menu;
    // MenuEvent type definition
    typedef void (Menu::* MenuEvent)();
    class ControlBase : public Object
    {
        public:
            ControlBase();
            virtual ~ControlBase();
        protected:
            Menu* m_Parent;
        private:
    };
}

#endif // CONTROLBASE_H
