#ifndef ME_LABEL_H
#define ME_LABEL_H

#include <SFML/Graphics.hpp>
#include <Menu/ControlBase.hpp>

namespace me
{
    class Label : public me::ControlBase //, sf::Text
    {
        public:
            Label(const sf::String& text);
            virtual ~Label();
            sf::String GetString() {return m_Text.getString();}
            void SetString(const sf::String& text) {m_Text.setString(text);}
            bool LoadFont(const sf::String& font = "Gentium-R.ttf");
            void Draw();
        protected:
            virtual void draw(sf::RenderTarget& target, sf::RenderStates states) const;
        private:
            sf::Font* m_Font;
            sf::Text m_Text;
    };
} // namespace me

#endif // ME_LABEL_H
