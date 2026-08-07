pipeline{
        agent any

        environment{
        VENV = "venv"
        }

        stages{
            stage('Checkout'){
                steps{
                    git branch: "main", url: "https://github.com/Poojaraghu-git/Playwright_Pytest_HR_Management_Web_Application.git"
                    }
            }

            stage('Setup Python Environment'){
                steps{
                    bat'''
                    python3 -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }

            stage('Run Pytest'){
                steps{
                    bat'''
                    call venv\\Scripts\\activate
                    pytest --html=report.html --self-contained-html
                    '''
                }
            }
        }

        post{
             always{
                   archiveArtifacts artifacts: "report.html", fingerprint: true
                    }
             failure{
                    echo "Test Failed. Please check the report for details."
                    }
             success{
                    echo "Test Passed. Please check the report for details."
                    }
             }

}