#include "Global.hpp"
#include "Menu/Label.hpp"

namespace me
{
    Label::Label(const sf::String& text)// : m_Text(text, *m_Font)
    {
        m_Font = new sf::Font();
        m_Text.setFont(*m_Font);
        LoadFont("Gentium-I.ttf");
        Log("Made Label");

        //m_Font.loadFromFile("fonts\\Gentium-R.ttf");
        //m_Font.loadFromFile("fonts\\Gentium-I.ttf");
        //m_Text.setFont(m_Font);
        m_Text.setString(text);
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
        if (!m_Font->loadFromFile("fonts\\" + font))
        {
            //me::Error("Font Loading Failed");
            return false;
        }
        //m_Text.setFont(m_Font);
        return true;
    }
} // namespace me
