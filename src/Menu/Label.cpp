#include "Global.hpp"
#include "Menu/Label.hpp"
#include "Game.hpp"

namespace me
{
    Label::Label(const sf::String& text, unsigned int size, const sf::Vector2f& pos, float rot)// : m_Text(text, *m_Font)
    {
        LoadFont();
        m_Text.setString(text);
        m_Text.setCharacterSize(size);
        m_Text.setPosition(pos);
        m_Text.setRotation(rot);
    }

    Label::~Label()
    {
    }

    void Label::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Text);
    }

    bool Label::LoadFont(const sf::String& font)
    {
        /*if (!m_Font->loadFromFile("fonts\\" + font))
        {
            //me::Error("Font Loading Failed");
            return false;
        }*/
        sf::Font* t = Game::GetInstance()->GetResourceManager()->GetFont(font);
        if (t == 0)
        {
            //delete t;
            return false;
        }
        m_Font = t;
        m_Text.setFont(*m_Font);
        return true;
    }
} // namespace me
