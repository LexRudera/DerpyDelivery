#ifndef ME_BUTTON_H
#define ME_BUTTON_H

#include <MenuControls/ControlBase.hpp>
#include "MenuControls/Label.hpp"
#include "Menu.hpp"

namespace me
{
    struct BtnStateStyle;
    class Button : public ControlBase
    {
        public:
            struct BtnStateStyle
            {
                BtnStateStyle(sf::Texture* tex, sf::Color outl, sf::Color fill, sf::Color text, float thcknss)
                {
                    Background = tex;
                    OutlineColour = outl;
                    FillColour = fill;
                    TextColour = text;
                    OutlineThickness = thcknss;
                }
                ~BtnStateStyle()
                {
                    delete Background;
                }

                sf::Texture* Background;
                sf::Color OutlineColour;
                sf::Color FillColour;
                sf::Color TextColour;
                float OutlineThickness;
            };

            Button(Menu* parent,
                   const sf::String& text,
                   const sf::Vector2f& size = sf::Vector2f(50,50),
                   const sf::Vector2f& pos = sf::Vector2f(),
                   float rot = 0);
            virtual ~Button();

            void tick();
            void draw(sf::RenderTarget& target, sf::RenderStates states) const;

            bool LoadTexture(const sf::String& strng);
            void SetOnClickFunction(MenuEvent Func) { OnClick = Func; }
            void SetString(const sf::String& t){ m_Text.SetString(t); }
        protected:
        private:
            void ApplyState(BtnStateStyle* Style);

            // Elements of a button
            Label m_Text;
            sf::RectangleShape m_Btn;

            // Function Delegates
            MenuEvent OnClick = 0;

            // Visual Styles
            BtnStateStyle* IdleStyle = 0;
            BtnStateStyle* DownStyle = 0;
            BtnStateStyle* HoverStyle = 0;
    };
} // namespace me

#endif // ME_BUTTON_H
