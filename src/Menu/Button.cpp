#include "Menu/Button.hpp"
#include "Global.hpp"

namespace me
{
    Button::Button(const sf::String& text,
                   const sf::Vector2f& size,
                   const sf::Vector2f& pos,
                   float rot) : m_Text(text), m_Btn(size)
    {
        setPosition(pos);
        setRotation(rot);

        OnClick = 0;
        DownStyle = 0;
        HoverStyle = 0;
        m_Btn.setFillColor(sf::Color(128,128,128));
        m_Btn.setOutlineColor(sf::Color(85,85,85));
        m_Btn.setOutlineThickness(3);

        //m_Text.setOrigin(0, m_Text.getLocalBounds().height);
        //m_Text.setPosition(sf::Vector2f(size.x/2, m_Btn.getLocalBounds().height/2));
        m_Text.setPosition(sf::Vector2f(size.x/2-m_Text.getLocalBounds().width/2, size.y/2-m_Text.getCharacterSize()/4*3));//-m_Text.getLocalBounds().height/2));
    }

    Button::~Button()
    {
        //dtor
    }

    void Button::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Btn, states);
        target.draw(m_Text, states);
    }
} // namespace me
