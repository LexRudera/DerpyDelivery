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
            bool IsScrolling() { return m_Scrolling; }
            void IsScrolling(bool a) { m_Scrolling = a; }
        protected:
            Menu* m_Parent;
        private:
            bool m_Scrolling = true;
    };
}

#endif // CONTROLBASE_H
