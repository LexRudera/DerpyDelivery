#ifndef ME_BUTTON_H
#define ME_BUTTON_H

#include <Menu/ControlBase.hpp>
#include "Menu\Label.hpp"

namespace me
{
    class Button : public ControlBase
    {
        public:
            Button(const sf::String& text,
                   const sf::Vector2f& pos = sf::Vector2f(),
                   const sf::Vector2f& size = sf::Vector2f(50,50),
                   float rot = 0);
            virtual ~Button();

            void draw(sf::RenderTarget& target, sf::RenderStates states) const;
            bool LoadTexture(const sf::String& strng);
        protected:
        private:
            Label m_Text;
            sf::RectangleShape m_Btn;
    };
} // namespace me

#endif // ME_BUTTON_H
