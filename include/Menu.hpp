#ifndef MENU_H
#define MENU_H

#include "Scene.hpp"
#include "MenuControls/ControlBase.hpp"

namespace me
{
    //---------------------------------------------------------
    // The virtual menu class.
    // A menu is not just a menu. It's always a specific type
    // of menu, like a main menu or options menu.
    //---------------------------------------------------------
    class Menu : public Scene
    {
        public:
            /** Default constructor */
            Menu();
            /** Default destructor */
            virtual ~Menu();
            void Tick();
            void Add(ControlBase* obj);
        protected:
        private:
    };
};

#endif // MENU_H
