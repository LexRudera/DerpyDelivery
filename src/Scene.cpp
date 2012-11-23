#include "Scene.hpp"
namespace me
{
    Scene::Scene()
    {
        //ctor
    }

    Scene::~Scene()
    {
        //dtor
    }

    void Scene::Tick()
    {

    }

    void Scene::Render(sf::RenderTarget& target, sf::RenderStates states)
    {
        for (unsigned int i = 0; i < m_Objects.capacity(); i++)
        {
            m_Objects[i]->draw(sf::RenderTarget& target, sf::RenderStates states);
        }
    }
}
