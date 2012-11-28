#include "Global.hpp"
#include "Menu/Label.hpp"

namespace me
{
    Label::Label(const sf::String& text)// : m_Text(text, m_Font)
    {
        //LoadFont("Gentium-R.ttf");
        Log("Made Label");

        m_Font.loadFromFile("fonts\\Gentium-R.ttf");
        m_Text.setFont(m_Font);
        m_Text.setString("Derp");

        std::cout << m_Text.getFont() << std::endl;
        std::cout << m_Text.getString().toAnsiString() << std::endl;
        std::cout << std::endl;
    }

    Label::~Label()
    {
    }

    void Label::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {

        std::cout << m_Text.getFont() << std::endl;
        std::cout << m_Text.getString().toAnsiString() << std::endl;
        std::cout << std::endl;
        sf::Font f;
        f.loadFromFile("fonts\\Gentium-R.ttf");
        sf::Text text("TestDerp",f);
        text.setPosition(20,30);
        target.draw(text);

        //Log("Label Draw");
        states.transform *= getTransform();
        target.draw(m_Text);
        Log("Label Drawn");
    }

    bool Label::LoadFont(const sf::String& font)
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
