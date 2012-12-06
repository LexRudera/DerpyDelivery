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

    void Scene::DoTick()
    {
        for (unsigned int i = 0; i < m_Objects.size(); i++)
        {
            //Log("Render loop: " + *((Label)m_Objects[i]).GetString());
            m_Objects[i]->tick();
        }
    }

    void Scene::Render(sf::RenderTarget& target)
    {
        for (unsigned int i = 0; i < m_Objects.size(); i++)
        {
            //Log("Render loop: " + *((Label)m_Objects[i]).GetString());
            target.draw(*m_Objects[i],sf::RenderStates::Default);
        }
    }
}
