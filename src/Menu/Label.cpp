#include "Global.hpp"
#include "Menu/Label.hpp"
#include "Game.hpp"

namespace me
{
    Label::Label(const sf::String& text, unsigned int size, const sf::Vector2f& pos, float rot)
    {
        LoadFont();
        m_Text.setString(text);
        m_Text.setCharacterSize(size);
        setPosition(pos);
        setRotation(rot);
    }

    Label::~Label()
    {
    }

    void Label::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        //states.transform *= getTransform();
        states.transform *= getTransform();
        target.draw(m_Text, states);
    }

    bool Label::LoadFont(const sf::String& font)
    {
        sf::Font* t = Game::GetInstance()->GetResourceManager()->GetFont(font);
        if (t == 0)
        {
            //delete t;
            return false;
        }
        m_Text.setFont(*t);
        return true;
    }
} // namespace me
