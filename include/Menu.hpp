#ifndef MENU_H
#define MENU_H

#include "Scene.hpp"
#include "Menu\ControlBase.hpp"

namespace me
{
    class Menu : public Scene
    {
        public:
            /** Default constructor */
            Menu();
            /** Default destructor */
            virtual ~Menu();
            void Tick();
            void Add(ControlBase* obj);
            static Menu* MainMenu();
        protected:
        private:
    };
};

#endif // MENU_H
