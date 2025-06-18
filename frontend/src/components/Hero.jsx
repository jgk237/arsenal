import React from 'react'

const players = [
  {
    name: 'Bukayo Saka',
    image: 'https://resources.premierleague.com/premierleague/photos/players/110x140/p223340.png',
    role: 'Right Winger',
  },
  {
    name: 'Martin Ødegaard',
    image: 'https://resources.premierleague.com/premierleague/photos/players/110x140/p184029.png',
    role: 'Captain / Midfielder',
  },
  {
    name: 'Mikel Arteta',
    image: 'https://resources.premierleague.com/premierleague/photos/players/110x140/man51018.png',
    role: 'Manager',
  },
]

export const Hero=()=> {
  return (
    <section className="bg-black text-white min-h-screen flex flex-col-reverse items-center justify-center px-4 md:flex-row md:justify-between overflow-hidden">
      <div className="text-center md:text-left max-w-xl space-y-6">
        <h1 className="text-4xl md:text-5xl font-extrabold leading-tight">
          Welcome to Arsenal Insights
        </h1>
        <p className="text-gray-300 text-lg md:text-xl">
          Dive into stats, stories, and match predictions. All things Arsenal — past and future — in one place.
        </p>
        <button className="px-6 py-3 bg-red-600 hover:bg-red-700 rounded-lg font-semibold transition">
          Explore Now
        </button>
      </div>

      <div className="max-w-xs w-full md:max-w-sm flex justify-center">
        <div className="relative bg-transparent rounded-lg overflow-hidden">
          <img
            src="https://resources.premierleague.com/premierleague/photos/players/110x140/p223340.png"
            alt="Bukayo Saka"
            className="w-full h-auto object-contain mix-blend-screen"
            style={{ backgroundColor: 'transparent' }}
            onError={(e) => {
              e.target.src = 'https://via.placeholder.com/110x140/000000/FFFFFF?text=Arsenal'
            }}
          />
        </div>
      </div>
      <div className="text-center md:text-left max-w-xl space-y-6">
        <h1 className="text-4xl md:text-5xl font-extrabold leading-tight">
          Welcome to Arsenal Insights
        </h1>
        <p className="text-gray-300 text-lg md:text-xl">
          Dive into stats, stories, and match predictions. All things Arsenal — past and future — in one place.
        </p>
        <button className="px-6 py-3 bg-red-600 hover:bg-red-700 rounded-lg font-semibold transition">
          Explore Now
        </button>
      </div>

      <div className="max-w-xs w-full md:max-w-sm flex justify-center">
        <div className="relative bg-transparent rounded-lg overflow-hidden">
          <img
            src="https://resources.premierleague.com/premierleague/photos/players/110x140/p223340.png"
            alt="Bukayo Saka"
            className="w-full h-auto object-contain mix-blend-screen"
            style={{ backgroundColor: 'transparent' }}
            onError={(e) => {
              e.target.src = 'https://via.placeholder.com/110x140/000000/FFFFFF?text=Arsenal'
            }}
          />
        </div>
      </div>
    </section>
  )
}