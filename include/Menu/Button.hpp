#ifndef ME_BUTTON_H
#define ME_BUTTON_H

#include <Menu/ControlBase.hpp>
#include "Menu\Label.hpp"

namespace me
{
    class Button : public ControlBase
    {
        public:
            Button();
            virtual ~Button();
        protected:
        private:
            Label* m_Text;
            sf::RectangleShape* m_Btn;
    };
} // namespace me

#endif // ME_BUTTON_H
