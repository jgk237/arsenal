import React from 'react'

export const Navbar = () => {
  return (
    <nav className="px-6 py-4 flex justify-between items-center shadow-lg">
      <div className="text-2xl font-bold tracking-wider text-white font-['Arial']">
        <span className="text-white">ARSENAL</span>
        <span className="text-[#FFFFFF] mx-1">|</span>
        <span className="text-[#023474]">FC</span>
      </div>
      <ul className="hidden md:flex space-x-8 text-sm font-semibold uppercase tracking-wider">
        <li className="text-[#EF0107] hover:text-[#023474] transition-colors duration-300">Home</li>
        <li className="text-[#EF0107]hover:text-[#023474] transition-colors duration-300">Players</li>
        <li className="text-[#EF0107] hover:text-[#023474] transition-colors duration-300">Matches</li>
        <li className="text-[#EF0107] hover:text-[#023474] transition-colors duration-300">History</li>
      </ul>
      <div className="md:hidden">
        <button className="text-[#EF0107] focus:outline-none">
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path 
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="3"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>
      </div>
    </nav>
  )
}