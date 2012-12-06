#include "MenuControls/Button.hpp"
#include "Global.hpp"
#include "InputManager.hpp"
#include "Game.hpp"

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

    void Button::tick()
    {
        // Sense the mouse and react accordingly.
        sf::Vector2i MPos = Game::Get()->GetInputManager()->GetMousePos();
        if (MPos.x > getPosition().x // Below the x pos
            && MPos.x < getPosition().x + m_Btn.getSize().x // Above the lower box bounds
            && MPos.y > getPosition().y // Past the y pos
            && MPos.y < getPosition().y + m_Btn.getSize().y) // Before the right box bounds
        {
            if (Game::Get()->GetInputManager()->IsButtonDown(sf::Mouse::Button::Left))
                Log("Mouse it clicked on '" + m_Text.GetString() + "'");
            //else
                //Log("Mouse is hovering over '" + m_Text.GetString() + "' - " + to_string(MPos.x) + " - " + to_string(MPos.y));
        }
    }
} // namespace me
