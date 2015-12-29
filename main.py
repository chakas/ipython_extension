from IPython.core.magic import Magics, line_magic, magics_class
from simple_salesforce import Salesforce
import pandas as pd

@magics_class
class SfMagics(Magics):
    @line_magic
    def sflogin(self, line='', setup='pass'):
    	opts, stmt = self.parse_options(line, 'u:p:t:l', posix=False,strict=False)
    	print opts

    	return login_into_sf(self,opts["u"], opts["p"], opts["t"],opts["l"])
    
def login_into_sf(self,username,password,token,url):
	sf = Salesforce(username=username,password=password,security_token=token,instance=url,sandbox=True)
	# data = sf.query("select id,lastname from contact limit 1000")
	ns = self.shell.user_ns
	ns['sfObject'] = sf

if __name__ == '__main__':
    ip = get_ipython()
    ip.register_magics(SfMagics)
