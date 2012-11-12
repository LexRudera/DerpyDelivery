#include "Scene.hpp"

me::Scene::Scene()
{
    //ctor
}

me::Scene::~Scene()
{
    //dtor
}

void me::Scene::Tick()
{

}

void me::Scene::Render()
{
    for (unsigned int i = 0; i < m_Objects.capacity(); i++)
    {
        m_Objects[i]->Draw();
    }
}
