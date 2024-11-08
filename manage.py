from app import create_app

# Create app instance
app = create_app("development")

# @manager.command
# def tests():
#     import unittest
#     tests = unittest.TestLoader().discover("tests")
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
 app.run()
