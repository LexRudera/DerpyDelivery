#include "Global.hpp"
#include "Menu/Label.hpp"

namespace me
{
    Label::Label(const sf::String& text) : m_Text(text, m_Font)
    {
        LoadFont("Gentium-R.ttf");
        m_Text.setColor(sf::Color::White);
        Log("Made Label");
    }

    Label::~Label()
    {
    }

    void Label::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        //Log("Label Draw");
        states.transform *= getTransform();
        target.draw(m_Text,states);
    }

    bool Label::LoadFont(const sf::String& font = "Gentium-R.ttf")
    {
        if (!m_Font.loadFromFile("fonts\\" + font))
        {
            //me::Error("Font Loading Failed");
            return false;
        }
        m_Text.setFont(m_Font);
        return true;
    }
} // namespace me
