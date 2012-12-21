#include "Background.hpp"
#include "Global.hpp"
#include "Game.hpp"

namespace me
{
    Background::Background()
    {
        //ctor
    }

    Background::~Background()
    {
        //dtor
    }

    void Background::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        //Render dat shit!
            //sf::Sprite t;
            //t.setTexture(*Game::Get()->GetResourceManager()->GetTexture("Pretty Pictured"));
        for (unsigned int i = 0; i< m_BgTextures.size(); i++)
        {
            //----------------------
            //THIS NEEDS FIXIN'!
            //----------------------
            Log("Let's draw backgrounds :3 " + to_string(m_BgTextures[i]->getTexture()));
            //target.draw(t,states);
            m_BgTextures[i]->setTexture(*Game::Get()->GetResourceManager()->GetTexture("Pretty Texture"));
            target.draw(*m_BgTextures[i],states);
        }
    }

    void Background::Add(sf::Texture* tex, const sf::Vector2f& pos, const sf::Vector2f& scl, float rot)
    {
        sf::Sprite* t = new sf::Sprite(*tex);
        t->setPosition(pos);
        t->setScale(scl);
        t->setRotation(rot);
        m_BgTextures.push_back(t);
    }
    void Background::Rearrange(unsigned int from, unsigned int to)
    {
        std::vector<sf::Sprite*>::iterator it = m_BgTextures.begin();
        sf::Sprite* t = m_BgTextures[from];

        m_BgTextures.erase(it+from);
        if (to >= m_BgTextures.size())
            m_BgTextures.push_back(t);
        else
            m_BgTextures.insert(it+to,t);
    }
    void Background::Remove(int at)
    {
        m_BgTextures.erase(m_BgTextures.begin() + at);
    }

    // Get to the actual sprite, so you can manupulate it,
    // realitve to the rest of the background.
    sf::Sprite* Background::GetLayer(int i)
    {
        return m_BgTextures[i];
    }
}
