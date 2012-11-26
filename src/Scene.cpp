#include "Scene.hpp"
#include "Global.hpp"

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

    void Scene::Render(sf::RenderTarget& target)
    {
        for (unsigned int i = 0; i < m_Objects.capacity(); i++)
        {
            target.draw(*m_Objects[i],sf::RenderStates::Default);
        }
    }
}
