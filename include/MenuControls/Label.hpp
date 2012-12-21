#ifndef ME_LABEL_H
#define ME_LABEL_H

#include <SFML/Graphics.hpp>
#include <MenuControls/ControlBase.hpp>

namespace me
{
    class Label : public ControlBase //, sf::Text
    {
        public:
            Label(const sf::String& text, unsigned int size = 20, const sf::Vector2f& pos = sf::Vector2f(), float rot = 0);
            virtual ~Label();
            const sf::String& GetString() const {return m_Text.getString();}
            void SetString(const sf::String& text) {m_Text.setString(text);}
            bool LoadFont(const sf::String& font = "Gentium");

            sf::FloatRect getLocalBounds() const { return m_Text.getLocalBounds(); }
            sf::FloatRect getGlobalBounds() const { return m_Text.getGlobalBounds(); }
            unsigned int getCharacterSize() const { return m_Text.getCharacterSize(); }
        protected:
            virtual void draw(sf::RenderTarget& target, sf::RenderStates states) const;
        private:
            sf::Text m_Text;
    };
} // namespace me

#endif // ME_LABEL_H
