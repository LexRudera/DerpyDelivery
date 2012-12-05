#ifndef ME_BUTTON_H
#define ME_BUTTON_H

#include <Menu/ControlBase.hpp>
#include "Menu\Label.hpp"

namespace me
{
    struct BtnStateStyle;
    class Button : public ControlBase
    {
        public:
            Button(const sf::String& text,
                   const sf::Vector2f& size = sf::Vector2f(50,50),
                   const sf::Vector2f& pos = sf::Vector2f(),
                   float rot = 0);
            virtual ~Button();

            void draw(sf::RenderTarget& target, sf::RenderStates states) const;
            bool LoadTexture(const sf::String& strng);
        protected:
        private:
            void ApplyState(BtnStateStyle* Style);
            Label m_Text;
            sf::RectangleShape m_Btn;
            void (*OnClick)();

            BtnStateStyle* IdleStyle;
            BtnStateStyle* DownStyle;
            BtnStateStyle* HoverStyle;
    };

    struct BtnStateStyle
    {
        BtnStateStyle();
        ~BtnStateStyle();

        sf::Texture* Background;
        float OutlineThickness;
    };
} // namespace me

#endif // ME_BUTTON_H
