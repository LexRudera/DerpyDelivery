#include "Scene.hpp"
#include "Global.hpp"
#include "menu\label.hpp"

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
        //Log("Tick");
    }

    void Scene::Render(sf::RenderTarget& target)
    {
        for (unsigned int i = 0; i < m_Objects.size(); i++)
        {
            //((Label*)m_Objects[i])->LoadFont("Gentium-R.ttf");
            //Log("Render loop: " + *((Label)m_Objects[i]).GetString());
            target.draw(*m_Objects[i],sf::RenderStates::Default);
        }
    }
}
