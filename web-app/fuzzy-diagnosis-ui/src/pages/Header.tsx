import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <nav className="bg-blue-600 text-white p-4">
      <div className="max-w-4xl mx-auto">
        <ul className="flex space-x-4 justify-center">
          <li><Link to="/survey" className="hover:underline">Survey</Link></li>
          <li><Link to="/result" className="hover:underline">Results</Link></li>
        </ul>
      </div>
    </nav>
  );
};

export default Header;