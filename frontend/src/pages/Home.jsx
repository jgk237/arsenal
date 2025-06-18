import React from 'react'
import { Navbar } from '../components/Navbar'

const Home = () => {
  return (
    <div 
      className="min-h-screen w-full bg-cover bg-center"
      style={{
        backgroundImage: `url('https://i.pinimg.com/1200x/5f/51/28/5f51285cf9d41aa348e151c0e1be0012.jpg')`,
      }}
    >
      <Navbar />
      <main className="min-h-[calc(100vh-4rem)] w-screen flex items-center justify-between px-4 md:px-16">
        {/* Left: Text Box */}
        <div className="flex-1 max-w-2xl py-12">
          <div className="bg-white/80 backdrop-blur-md p-8 rounded-xl shadow-md">
            <h1 className="text-5xl md:text-6xl font-extrabold mb-6 leading-tight text-black">
              Welcome to <span className="text-red-700">Arsenal FC</span>
            </h1>
            <p className="text-xl md:text-2xl text-gray-800">
              Glory through harmony. <br /> Built in London. Made for greatness.
            </p>
          </div>
        </div>

        {/* Right: Image */}
        <div className="flex-1 hidden md:flex justify-end">
          <img
            src="https://assets.goal.com/images/v3/bltfbce25d776edca6a/0d60894abb942122d4ecbfe8657d4f2cf59e4eee.jpg?auto=webp&format=pjpg&width=3840&quality=60"
            alt="Arsenal Visual"
            className="h-[80vh] object-contain"
          />
        </div>
      </main>
    </div>
  )
}

export default Home